import { LOGOUT } from "./types";

import axios from "axios";
axios.defaults.withCredentials = true;

export const googleAuthenticate = (state, code) => async (dispatch) => {
  if (state && code && !localStorage.getItem("access")) {    
    axios({
      method: 'post',
      url: 'http://localhost:8000/auth/o/google-oauth2/',
      params: {
        state: state,
        code: code
      }
    })
    .then(response => {
      console.log(response.data);
    });  
    }
};

export const logout = () => (dispatch) => {
  dispatch({
    type: LOGOUT,
  });
};
