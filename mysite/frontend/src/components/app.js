import React, { Component } from "react";
import { render } from "react-dom";
import {Route, NavLink, HashRouter} from "react-router-dom";

import Fetch_data from "./fetch_info/fetch_data";
import Input from "./input/input.js";

class App extends Component {
	render() {
		return (
			<HashRouter>
				<div>
					<ul className="paths">
						<li><NavLink to="/register">register</NavLink></li>
						<li><NavLink to="/info">my information</NavLink></li>
					</ul>
					<div className="content">
						<Route path="/register" component={Input} />
						<Route path="/info" component={Fetch_data}  />
					</div>
				</div>
			</HashRouter>
		);
	}
}

export default App;

const container = document.getElementById("app");
render(<App />, container);


