
from typing import Any, Text, Dict, List

import rasa_sdk
from rasa_sdk.executor import CollectingDispatcher


class ActionPerson(rasa_sdk.Action):

    def name(self) -> Text:
        return "action_person"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: rasa_sdk.Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        person_entity = next(tracker.get_latest_entity_values('person'),None)

        if person_entity:
            dispatcher.utter_message(text=f"Hi {person_entity} how can i help you?")
        else:
            dispatcher.utter_message(text=f"I'm sorry,something went wrong")


         return []