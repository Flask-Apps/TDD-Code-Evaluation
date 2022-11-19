import renderer from "react-test-renderer";
import React from "react";
import { shallow } from "enzyme";

import UsersList from "../UsersList";

const users = [
  {
    active: true,
    email: "natsu@fairytail.com",
    id: 1,
    username: "natsu",
  },
  {
    active: true,
    email: "lucy@fairytail.com",
    id: 2,
    username: "lucy",
  },
];

test("UsersList renders properly", () => {
  // wrapper to create UserList component
  // and retrieve the o/p and make assertions
  // against it

  // with shallow rendering we can test the component
  // in total isolation this helps to ensure child
  // componenets donot indirectly affect assertions
  const wrapper = shallow(<UsersList users={users} />);
  const element = wrapper.find("h4");

  expect(element.length).toBe(2);
  expect(element.get(0).props.className).toContain("users");
  expect(element.get(0).props.children).toBe("natsu");
});

// add a snapshot test to ensure the UI doesnot change
test("UsersList renders a snapshot properly", () => {
  const tree = renderer.create(<UsersList users={users} />).toJSON();
  expect(tree).toMatchSnapshot();
});
