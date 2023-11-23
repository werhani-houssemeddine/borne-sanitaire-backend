const serverResponseTemplate = document.querySelector('#fetch-response-template');
const invalidIDTemplate      = document.querySelector('#invalid-id-template');
const rejectTemplate         = document.querySelector('#reject-agent-template')
const formTemplate           = document.querySelector('#add-agent-template');

const mainContainer          = document.querySelector('#main-container');

class Utils{
  static getQueries() {
    const url = document.location.search.replace('?', '');
    
    if (url === "") return null;
    
    const listOfQueries = {};
    url.split('&').map(element => {
      if(element !== undefined) {
        element = element.split("=");
        listOfQueries[element[0]] = element[1];
      }
    });
  
    return listOfQueries;
  }

  static getAgentId(agentQuery) {
  
    if (agentQuery === null) return null;
    if (agentQuery['agent'] === null) return null;
  
    return agentQuery['agent'];
  }

  static constructURL(endpoint) {
    const BASE_URL    = location.origin;

    const AGENT_QUERY = { agent: this.getAgentId(this.getQueries()) };
    const queryString = Object.keys(AGENT_QUERY)
                              .map(key => `${key}=${encodeURIComponent(AGENT_QUERY[key])}`)
                              .join('&');
  
    return `${BASE_URL}${endpoint}?${queryString}`;
  }
}

class Template{
  static addContentToTemplate(content) {
    mainContainer.innerHTML = '<p class="invalid_id"> ' + content + '</p>';;
  }
}


window.addEventListener('load', async() => {
  try {
    const response = await fetch(Utils.constructURL('/api/client/agent/check-request-agent/'));

    //? Removing the wait effect when we receive data from the server
    mainContainer.classList.remove('wait_background');

    if(response.status === 200){
      const templateContent = formTemplate.content.cloneNode(true);
      mainContainer.innerHTML = "";
      mainContainer.append(templateContent);
      addForm();
      return;
    }

    console.log({ response });

    throw Error("Nope");
    
  } catch (error) {
    console.error({ error });
    Template.addContentToTemplate(`
        We regret to inform you that your request is considered outdated and cannot be processed in its current form.
        We appreciate your understanding, if you have any questions or require further clarification, please call
        your associations.
    `);
  }
});

window.addEventListener('unhandledrejection', e => {
  e.preventDefault();
});
