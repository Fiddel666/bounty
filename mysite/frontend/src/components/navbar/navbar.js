import React, { Component } from "react";
import { render } from "react-dom";
import {Route, NavLink, HashRouter} from "react-router-dom";

import Fetch_data from "./fetch_info/fetch_data";
import Input from "./input/input.js";
import Login from "./login/login.js";
import Logout from "./logout/logout.js";
import Logo from "./logo/logo.js";

class Navbar extends Component {
	render() {
		return (
			<div>
				<Logo />
				
				<HashRouter>
					<div>
						<div className="paths">
							<div><NavLink className="b" to="/register">register</NavLink></div>
							<div><NavLink className="b" to="/info">my information</NavLink></div>
							<div><NavLink className="b" to="/login">login</NavLink></div>
							<div><Logout /></div>
						</div>
						<div className="content">
							<Route path="/register" component={Input} />
							<Route path="/info" component={Fetch_data}  />
							<Route path="/login" component={Login}  />
						</div>
					</div>
				</HashRouter>
			</div>
		);
	}
}

export default Navbar;



