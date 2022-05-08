import React from 'react';

const Header = () => {
  return (
    <nav className="navbar navbar-dark bg-dark">
      <div className="container-fluid">
        <a className="navbar-brand" href="/job/">Job</a>
        <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavDropdown"
                aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
          <span className="navbar-toggler-icon"></span>
        </button>
        <div className="collapse navbar-collapse" id="navbarNavDropdown">
          <ul className="navbar-nav">
            <li className="nav-item">
              <a className="nav-link active" aria-current="page" href="/job/">Job</a>
            </li>
            <li className="nav-item">
              <a className="nav-link" href="/auth/registration/">Register!</a>
            </li>
            <li className="nav-item">
              <a className="nav-link" href="/auth/login/">Login!</a>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  );
};

export default Header;