function addForm() {
  try {
    const form = document.querySelector('form');
    if (form != null) {
      const user_name = form.querySelector('#user_name');
      const password  = form.querySelector('#password');

      if(user_name != null && password != null) {

        const queries = Utils.getQueries();

        if(queries === null) throw new Error();
        if(queries.reject === "true") return handleRejection();

        form.addEventListener('submit', handleSubmitForm(user_name, password));
        return;
      }
    }

    throw new Error();

  } catch (error) {
    console.error({ error: "FORM ERROR "});
    throw error;
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
        const response = await fetch(Utils.constructURL('/api/client/signup/'), {
          method : 'POST',
          body   : JSON.stringify(userData),
          headers: { 'Content-Type': 'application/json' }
        });
  
        if (response.status >= 200 && response.status <= 299) {

        }
        
        throw new Error();
        
      } catch (error) {
        //! INVALID SIGN UP
      }
      
    } else {
      if(getUserNameLength < 4) {
        const usernameErrorMessageContainer = document.querySelector('.username-error');

        usernameErrorMessageContainer.textContent = 'Invalid Username'
        usernameErrorMessageContainer.classList.remove('hidden');
      } else {
        const passwordErrorMessageContainer = document.querySelector('.password-error');

        passwordErrorMessageContainer.textContent = 'Invalid Password length'
        passwordErrorMessageContainer.classList.remove('hidden');
      }
    }
  }
}

function handleRejection(agent_id) {
  sendRejectRequest(agent_id).then(res => {
    let messageToShow = '';
    if (res === "SUCCESS") {
      messageToShow = `We regret to inform you that we are rejecting this request. 
                       We will notify the sender accordingly. We appreciate your understanding
                       and hope for another opportunity to be of service in the future.`;
    } else {
      messageToShow = `Your submission has been refused. Please try again later. 
                       We apologize for any inconvenience this may have caused`;
    }

    Template.addContentToTemplate(messageToShow);

  }).catch(() => {}); 
}

async function sendRejectRequest(agent_id) {
  try {
    await fetch(constructURL(`/api/client/agent/reject/&agent=${agent_id}`));
    if(response === 204) {
      return "SUCCESS";
    } else {
      return "FAILLURE";
    }
  } catch (error) {
    return "FAILLURE";
  }
}