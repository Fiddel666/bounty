import React, { Component } from "react";
import { render } from "react-dom";

import Navbar from "./navbar/navbar.js"

class App extends Component {
	render() {
		return (
			<Navbar />
		);
	}
}

export default App;

const container = document.getElementById("app");
render(<App />, container);


