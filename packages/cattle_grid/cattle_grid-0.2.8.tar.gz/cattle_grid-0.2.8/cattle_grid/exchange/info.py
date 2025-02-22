from cattle_grid.model.extension import MethodInformationModel

exchange_method_information = [
    MethodInformationModel(
        module="cattle_grid.exchange",
        routing_key="send_message",
        description="Takes an activity and sends it to its recipients",
    ),
    MethodInformationModel(
        module="cattle_grid.exchange",
        routing_key="update_actor",
        description="Updates an actor",
    ),
    MethodInformationModel(
        module="cattle_grid.exchange",
        routing_key="delete_actor",
        description="Deletes an actor",
    ),
]
"""Information about the methods defined on the ActivityExchange
by default"""
