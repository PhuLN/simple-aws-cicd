exports.handler = async (event) => {
    const response = {
        ...event.Payload,
        nodeProperty: "Added a new property via the Node Lambda v2"
    };
    
    return response;
};
