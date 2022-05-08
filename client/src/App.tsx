import React from "react";
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap.min';
import { Routes, Route } from "react-router-dom";
import RegistrationPage from "./pages/RegistrationPage";
import LoginPage from "./pages/LoginPage";
import WelcomePage from "./pages/WelcomePage";

function App() {
  return (
      <Routes>
        <Route path="/" element={<WelcomePage />}/>
        <Route path="/auth/registration/" element={<RegistrationPage />}/>
        <Route path="/auth/login/" element={<LoginPage />}/>
      </Routes>
  )
}

export default App;
