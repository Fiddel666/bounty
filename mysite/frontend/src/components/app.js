import React, { Component } from "react";
import { render } from "react-dom";

import Scores_info from "./fetch_info/scores_info";
import House_info from "./fetch_info/house_info";
import Users_info from "./fetch_info/users_info";

class App extends Component {
	render() {
		return (
			<div>
				<h1>
					Scores information
				</h1>
				<Scores_info />
				
				<h1>
					House information
				</h1>
				<House_info />
				
				<h1>
					Users information
				</h1>
				<Users_info />
			</div>
		);
	}
}

export default App;

const container = document.getElementById("app");
render(<App />, container);