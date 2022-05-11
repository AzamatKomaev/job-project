import React from 'react';
import Header from "../components/common/Header";
import RegistrationForm from "../components/auth/forms/RegistrationForm";

const RegistrationPage = () => {
  return (
    <div>
      <Header/><br/>
      <RegistrationForm/>
    </div>
  );
};

export default RegistrationPage;