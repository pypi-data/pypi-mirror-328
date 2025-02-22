"""Implements a vanilla playback strategy, offloading everything to the model.

    Send in a series of screenshots to GPT-4 and then ask GPT-4 to describe what
    happened. Then give it the sequence of actions (in concrete coordinates and
    keyboard inputs), as well as your proposed modification in natural language.
    Ask it to output the new action sequence.
    ...
    ...add [the current state to the prompt at every time step]
        --LunjunZhang

1. Given the recorded states, describe what happened
2. Given the description of what happened, proposed modifications in natural language
instructions, the current state, and the actions produced so far, produce the next
action.
"""

from pprint import pformat

from openadapt import adapters, models, strategies, utils
from openadapt.custom_logger import logger

PROCESS_EVENTS = True
INCLUDE_WINDOW_DATA = False


class VanillaReplayStrategy(strategies.base.BaseReplayStrategy):
    """Vanilla replay strategy that replays ActionEvents modified by an LMM directly.

    If AGI or GPT6 happens, this script should be able to suddenly do the work.
        --LunjunZhang
    """

    def __init__(
        self,
        recording: models.Recording,
        instructions: str = "",
        process_events: bool = PROCESS_EVENTS,
    ) -> None:
        """Initialize the VanillaReplayStrategy.

        Args:
            recording (models.Recording): The recording object.
            instructions (str): Natural language instructions
                for how recording should be replayed.
            process_events (bool): Flag indicating whether to process the events.
              Defaults to True.
        """
        super().__init__(recording)
        self.instructions = instructions
        self.process_events = process_events
        self.action_history = []
        self.action_event_idx = 0

        self.recording_description = describe_recording(
            self.recording,
            self.process_events,
        )

    def get_next_action_event(
        self,
        screenshot: models.Screenshot,
        window_event: models.WindowEvent,
    ) -> models.ActionEvent | None:
        """Get the next ActionEvent for replay.

        Args:
            screenshot (models.Screenshot): The screenshot object.
            window_event (models.WindowEvent): The window event object.

        Returns:
            models.ActionEvent or None: The next ActionEvent for replay or None
              if there are no more events.
        """
        if self.process_events:
            action_events = self.recording.processed_action_events
        else:
            action_events = self.recording.action_events

        self.action_event_idx += 1
        num_action_events = len(action_events)
        if self.action_event_idx >= num_action_events:
            raise StopIteration()
        logger.debug(f"{self.action_event_idx=} of {num_action_events=}")

        action_event = generate_action_event(
            screenshot,
            window_event,
            action_events,
            self.action_history,
            self.instructions,
        )
        if not action_event:
            raise StopIteration()

        self.action_history.append(action_event)
        return action_event

    def __del__(self) -> None:
        """Log the action history."""
        action_history_dicts = [
            action.to_prompt_dict() for action in self.action_history
        ]
        logger.info(f"action_history=\n{pformat(action_history_dicts)}")


def describe_recording(
    recording: models.Recording,
    process_events: bool,
    include_window_data: bool = INCLUDE_WINDOW_DATA,
) -> str:
    """Generate a natural language description of the actions in the recording.

    Given the recorded states, describe what happened.

    Args:
        recording (models.Recording): the recording to describe.
        process_events (bool): flag indicating whether to process the events.
        include_window_data (bool): flag indicating whether to incldue accessibility
            API data in each window event.

    Returns:
        (str) natural language description of the what happened in the recording.
    """
    if process_events:
        action_events = recording.processed_action_events
    else:
        action_events = recording.action_events
    action_dicts = [action.to_prompt_dict() for action in action_events]
    window_dicts = [
        action.window_event.to_prompt_dict(include_window_data)
        for action in action_events
    ]
    action_window_dicts = [
        {
            "action": action_dict,
            "window": window_dict,
        }
        for action_dict, window_dict in zip(action_dicts, window_dicts)
    ]
    images = [action.screenshot.image for action in action_events]
    system_prompt = utils.render_template_from_file(
        "prompts/system.j2",
    )
    prompt = utils.render_template_from_file(
        "prompts/describe_recording.j2",
        action_windows=action_window_dicts,
    )
    prompt_adapter = adapters.get_default_prompt_adapter()
    recording_description = prompt_adapter.prompt(
        prompt,
        system_prompt,
        images,
    )
    return recording_description


def generate_action_event(
    current_screenshot: models.Screenshot,
    current_window_event: models.WindowEvent,
    recorded_actions: list[models.ActionEvent],
    replayed_actions: list[models.ActionEvent],
    instructions: str,
) -> models.ActionEvent:
    """Modify the given ActionEvents according to the given replay instructions.

    Given the description of what happened, proposed modifications in natural language
    instructions, the current state, and the actions produced so far, produce the next
    action.

    Args:
        current_screenshot (models.Screenshot): current state screenshot
        current_window_event (models.WindowEvent): current state window data
        recorded_actions (list[models.ActionEvent]): list of action events from the
            recording
        replayed_actions (list[models.ActionEvent]): list of actions produced during
            current replay
        instructions (str): proposed modifications in natural language
            instructions

    Returns:
        (models.ActionEvent) the next action event to be played, produced by the model
    """
    current_image = current_screenshot.image
    current_window_dict = current_window_event.to_prompt_dict()
    recorded_action_dicts = [action.to_prompt_dict() for action in recorded_actions]
    replayed_action_dicts = [action.to_prompt_dict() for action in replayed_actions]

    system_prompt = utils.render_template_from_file(
        "prompts/system.j2",
    )
    prompt = utils.render_template_from_file(
        "prompts/generate_action_event.j2",
        current_window=current_window_dict,
        recorded_actions=recorded_action_dicts,
        replayed_actions=replayed_action_dicts,
        replay_instructions=instructions,
    )
    prompt_adapter = adapters.get_default_prompt_adapter()
    content = prompt_adapter.prompt(
        prompt,
        system_prompt,
        [current_image],
    )
    action_dict = utils.parse_code_snippet(content)
    logger.info(f"{action_dict=}")
    if not action_dict:
        # allow early stopping
        return None
    action = models.ActionEvent.from_dict(action_dict)
    logger.info(f"{action=}")
    return action
