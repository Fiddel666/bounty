import React, { Component } from "react";
import { render } from "react-dom";
import axios from "axios";

class Login extends Component {
	constructor(props) {
		super(props);
		this.state = {	username : '',
						password : ''
					};
		this.handleInput = this.handleInput.bind(this);
		this.login = this.login.bind(this);
		
		// set to automatically use django token
		axios.defaults.xsrfCookieName = 'csrftoken';
		axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
	}
	
	handleInput(event) {
		this.setState(
			{[event.target.name]: event.target.value},
			function (){ //callback function to use updated state
				console.log(this.state);
			}
		);
		console.log(this.state);
	}
	
	// send data to server here
	login(event) {
		// put data in form so data appear in POST
		var form_data = new FormData();
		for(var key in this.state){
			form_data.append(key, this.state[key]);
		}
		
		return axios.post('http://127.0.0.1:8000/bounty/login/', form_data)
		.then(res => console.log(res))
		.catch(err => console.error(err));
	}
	
	render() {
		return(
			<label>
				username:
				<input
					name="username"
					type="text"
					onChange={this.handleInput}
				/>
				
				<br />
				
				password:
				<input
					name="password"
					type="text"
					onChange={this.handleInput}
				/>
				
				<h5>
					{this.state.user}
				</h5>
				
				<button onClick={this.login}>
					login
				</button>
			</label>
		)
	}
}

export default Login;

