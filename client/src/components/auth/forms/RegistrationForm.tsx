import React, {useState} from 'react';
import {AuthApi} from "../../../api/auth";

interface IRegistrationState {
  username?: Array<string> | null,
  first_name?: Array<string> | null,
  last_name?: Array<string> | null,
  role?: Array<string> | null,
  password?: Array<string> | null,
  password2?: Array<string> | null,
  email?: Array<string> | null
}

const RegistrationForm = () => {
  const [errors, setErrors] = useState<IRegistrationState>({
    username: null,
    first_name: null,
    last_name: null,
    role: null,
    password: null,
    password2: null,
    email: null
  });

  const [username, setUsername] = useState<string>("");
  const [firstName, setFirstName] = useState<string>("");
  const [lastName, setLastName] = useState<string>("");
  const [role, setRole] = useState<string>("Choose role");
  const [password, setPassword] = useState<string>("");
  const [password2, setPassword2] = useState<string>("");
  const [email, setEmail] = useState<string>("");

  const handleRegisterUserButton = async() => {
    if (password !== password2) {
      setErrors({
        password2: ['The password are not equal.']
      });
      return ;
    }

    const response = await AuthApi.create({
      username: username,
      first_name: firstName,
      last_name: lastName,
      role: role,
      password: password,
      email: email
    })

    if (response.status === 201) {
    } else {
      setErrors(response.data)
    }
  }

  return (
    <div className="container col-10 col-sm-8 col-md-6 col-lg-4">
      <div className="form-group">
        <label htmlFor="email">Email address</label>
        <input
          type="email"
          className="form-control"
          id="email"
          placeholder="Enter email"
          value={email}
          onChange={e => setEmail(e.target.value)}
        />
        {errors.email ? <p className="text-danger">{errors.email[0]}</p> : null}
      </div>
      <div className="form-group" style={{marginTop: "10px"}}>
        <label htmlFor="username">Username</label>
        <input
          type="text"
          className="form-control"
          id="username"
          placeholder="Username"
          value={username}
          onChange={e => setUsername(e.target.value)}
        />
        {errors.username ? <p className="text-danger">{errors.username[0]}</p> : null}
      </div>
      <div className="form-group" style={{marginTop: "10px"}}>
        <label htmlFor="first_name">First Name</label>
        <input
          type="text"
          className="form-control"
          id="first_name"
          placeholder="First name"
          value={firstName}
          onChange={e => setFirstName(e.target.value)}
        />
        {errors.first_name ? <p className="text-danger">{errors.first_name[0]}</p> : null}
      </div>
      <div className="form-group" style={{marginTop: "10px"}}>
        <label htmlFor="last_name">Last Name</label>
        <input
          type="text"
          className="form-control"
          id="last_name"
          placeholder="Last name"
          value={lastName}
          onChange={e => setLastName(e.target.value)}
        />
        {errors.last_name ? <p className="text-danger">{errors.last_name[0]}</p> : null}
      </div>
      <div className="form-group" style={{marginTop: "10px"}}>
        <label htmlFor="password1">Password</label>
        <input
          type="password"
          className="form-control"
          id="password1"
          placeholder="Password"
          value={password}
          onChange={e => setPassword(e.target.value)}
        />
        {errors.password ? <p className="text-danger">{errors.password[0]}</p> : null}
      </div>
      <div className="form-group" style={{marginTop: "10px"}}>
        <label htmlFor="password2">Repeat password</label>
        <input
          type="password"
          className="form-control"
          id="password2"
          placeholder="Repeat password"
          value={password2}
          onChange={e => setPassword2(e.target.value)}
        />
        {errors.password2 ? <p className="text-danger">{errors.password2[0]}</p> : null}
      </div>
      <div className="form-group" style={{marginTop: "10px"}}>
        <label htmlFor="role">Role</label>
        <select
          className="form-select"
          value={role}
          onChange={e => setRole(e.target.value)}
          aria-label="Default select example"
        >
          <option value="">Choose role</option>
          <option value="employee">Employee</option>
          <option value="employer">Employer</option>
        </select>
        {errors.role ? <p className="text-danger">{errors.role[0]}</p> : null}
      </div>
      <br/>
      <button className="btn btn-primary" onClick={handleRegisterUserButton}>Register!</button>
    </div>
  );
};

export default RegistrationForm;