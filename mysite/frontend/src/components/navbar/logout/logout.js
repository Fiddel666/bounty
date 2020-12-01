import React, { Component } from "react";
import { render } from "react-dom";
import axios from "axios";

class Logout extends Component {
	// send data to server here
	logout(event) {
		return axios.post('http://127.0.0.1:8000/bounty/logout/')
		.then(res => console.log(res))
		.catch(err => console.error(err));
	}
	
	render() {
		return(	<a className="b" onClick={this.logout} href="#">
					logout
				</a>
		)
	}
}

export default Logout;

