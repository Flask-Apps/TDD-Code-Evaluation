import React, { Component } from "react";
import axios from "axios";
import { createRoot } from 'react-dom/client'

// this component runs automatically when an instance is created
// behind the scenes
class App extends Component {
  // eslint-disable-next-line no-useless-constructor
  constructor() {
    super();
    // add state property to the class and 
    // sets users to an empty array
    this.state = {
      users: []
    }
  }
  componentDidMount() {
    this.getUsers();
  };
  getUsers() {
    // console.log("Pokemon")
    axios.get(`${process.env.REACT_APP_USERS_SERVICE_URL}/users`)
    .then((res) => { this.setState({ users: res.data.data.users }); })
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
            {
              this.state.users.map((user) => {
                return (
                  <h4
                    key={ user.id }
                    className="card card-body bg-light"
                  >
                    { user.username }
                  </h4>
                )
              }
            )}
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
