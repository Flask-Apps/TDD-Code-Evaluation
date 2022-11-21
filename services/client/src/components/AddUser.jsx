import React from "react";

const AddUser = (props) => {
  return (
    <form>
      <div className="form-group">
        <input
          name="username"
          className="form-control input-lg"
          type="text"
          placeholder="Enter a username"
          required
        />
      </div>
      <div className="form-group">
        <input
          name="email"
          className="form-control input-lg"
          type="email"
          placeholder="Enter an email"
          required
        />
      </div>
        <input
          name="submit"
          className="btn btn-primary btn-lg btn-block"
          type="submit"
          value="Submit"
        />
    </form>
  );
};

export default AddUser;
