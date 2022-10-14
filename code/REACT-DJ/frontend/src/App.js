/* import logo from './logo.svg';*/
/* import './App.css'; */
import React from "react";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import Welcome from "./components/Welcome";
import Signup from "./components/Signup";
import Login from "./components/Login";
import { Provider } from "react-redux";
import Layout from "./components/Layout";
import store from "./store";

import Home from "./components/Home";

function App() {
  return (
    <div>
      <Provider store={store}>
        <BrowserRouter>
          <Layout>
            <Routes>
              <Route exact path="/" element={<Welcome />} />
              <Route exact path="/home" element={<Home />} />
              <Route path="/login" element={<Login />} />
              <Route path="/signup" element={<Signup />} />
            </Routes>
          </Layout>
        </BrowserRouter>
      </Provider>
    </div>
  );
}

// import React from "react";
// import ReactDOM from "react-dom";
// import { GoogleLogin } from "react-google-login";

// // import "./styles.css";

// const responseGoogle = response => {
//   console.log(response);
// };

// function App() {
//   return (
//     <div className="App">
//       <h1>Hello CodeSandbox</h1>
//       <h2>Start editing to see some magic happen!</h2>

//       <GoogleLogin
//         clientId="917537609153-lpfjkd2e0ca4otak7focgqs1mbv7g2ut.apps.googleusercontent.com"
//         buttonText="Login"
//         onSuccess={responseGoogle}
//         onFailure={responseGoogle}
//       />
//     </div>
//   );
// }

// const rootElement = document.getElementById("root");
// ReactDOM.render(<App />, rootElement);
export default App;
