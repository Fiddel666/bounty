import React, { Component } from "react";
import { render } from "react-dom";

class Users_info extends Component {
	constructor(props) {
		super(props);
		this.state = {
			data: [],
			loaded: false,
			placeholder: "Loading"
		};
	}
	
	// before rendering requesting for DATA in json format
	componentDidMount() {
		fetch("bounty/api/users")
			.then(response => {
				if (response.status > 400) {
					return this.setState(() => {
						return { placeholder: "Something went wrong!" };
					});
				}
				
				return response.json();
			})
			
			.then(data => {
				this.setState(() => {
					return {
						data,
						loaded: true
					};
				});
			});
	}

	render() {
		return (
			<ul>
				{this.state.data.map(user => {
					return (
						<li key={user.id}>
							{user.user} - {user.level} - {user.belt}  - {user.status} - {user.warning} - {user.house}
						</li>
					);
				})}
			</ul>
		);
	}
}

export default Users_info;