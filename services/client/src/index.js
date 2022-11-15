import React, { Component } from "react";
import axios from "axios";
import { createRoot } from 'react-dom/client'

// this component runs automatically when an instance is created
// behind the scenes
class App extends Component {
  // eslint-disable-next-line no-useless-constructor
  constructor() {
    super();
    this.getUsers();
  }
  getUsers() {
    // console.log("Pokemon")
    axios.get(`${process.env.REACT_APP_USERS_SERVICE_URL}/users`)
    .then((res) => { console.log(res); })
    .catch((err) => { console.log(err); })
  }
  render() {
    return (
      <div className="container">
        <div className="row">
          <div className="col-md-4">
            <br />
            <h1>All Users</h1>
            <hr />
            <br />
          </div>
        </div>
      </div>
    );
  }
}

const root = createRoot(document.getElementById('root'))
// mount the App to the DOM into the HTML element
// with an ID of root
root.render(<App />);
