exports.handler = async (event) => {
    const response = {
        ...event.response,
        nodeProperty: "Added a new property via the Node Lambda"
    };
    
    return response;
};
