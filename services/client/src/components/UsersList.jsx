import React from "react";

// we can pass state to a component with either
// props or state
// Props: data flows down via props (from state to props, read-only)
// State: data is tied to a component, read and write
const UsersList = (props) => {
  return (
    <div>
      {props.users.map((user) => {
        return (
          <h4 key={user.id} className="users card card-body bg-light">
            {user.username}
          </h4>
        );
      })}
    </div>
  );
};

export default UsersList;
