const form = document.querySelector('form');
if (form != null) {
  const user_name = form.querySelector('#user_name');
  const password  = form.querySelector('#password');

  if(user_name != null && password != null) {

    const agentQuery = getQueries();

    if(agentQuery === null) {
      console.error("ERROR OCCURED WHEN PARSING THE URL");
      setTimeout(() => window.close(), 2000); //! Close the window after 2s
    } else {
      form.addEventListener('submit', handleSubmitForm(user_name, password, agentQuery));
    }

  } else {
    console.error("ONE OF THE USERNAME OR PASSWORD IS MISSING");
  }
}

function handleSubmitForm(user_name, password) {
  return async (event) => {
    
    event.preventDefault();

    const trimValue = inputElement => inputElement.value.trim();

    const userData = { user_name: trimValue(user_name), password: trimValue(password) };

    const getUserNameLength = userData.user_name.length;
    const getPasswordLength = userData.password.length;


    //? This will work perfectly fine in this example. However, if 'validInputs' is a function 
    //? or an object property, it is better to check the length when the event occurs, not at
    //? compile time. As mentioned before, our example is completely fine because we invoke
    //? the function when we submit the button.

    //? const validInputs = () => getUserNameLength >= 4 && getPasswordLength >= 10;
    //? if (validInputs() === true)

    const validInputs       = getUserNameLength >= 4 && getPasswordLength >= 10;

    if(validInputs === true){

      try{
        const response = await fetch(constructURL(), {
          method : 'POST',
          body   : JSON.stringify(userData),
          headers: { 'Content-Type': 'application/json' }
        });
  
        const data = await response.json();
        alert("SIGN UP SUCCESSFULLY")
        setTimeout(() => window.close(), 3000);
        //! SIGN UP SUCCESSFULLY
      } catch (error) {
        //! INVALID SIGN UP
      }
      
    } else {
      console.log({ userData });
      console.error("DATA INVALID");
    }
  }
}

function getQueries() {
  const url = document.location.search.replace('?', '');
  
  if (url === "") return null;

  return url.split('&').map(element => {
    if(element !== undefined) {
      element = element.split("=");
      return { [element[0]]: element[1] }
    }
  });
}

function getAgentId(agentQuery) {
  for(let q of agentQuery) {
    if('agent' in q && q['agent'] !== undefined) {
      return q['agent'];
    }
  }
}

function constructURL() {
  const BASE_URL    = location.origin;
  const ENDPOINT    = '/api/client/signup/';

  const AGENT_QUERY = { agent: getAgentId(getQueries()) };
  const queryString = Object.keys(AGENT_QUERY)
                            .map(key => `${key}=${encodeURIComponent(AGENT_QUERY[key])}`)
                            .join('&');

  return `${BASE_URL}${ENDPOINT}?${queryString}`;
}