// to configure enzyme to use the react 16 adapter
import { configure } from "enzyme";
import Adapter from "enzyme-adapter-react-16";

configure({ adapter: new Adapter() });
// tests by default tests is run in watch mode i.e it'll
// re-run every time we save a file
