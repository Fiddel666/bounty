import React, { Component } from "react";
import { render } from "react-dom";

class House_info extends Component {
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
		fetch("bounty/api/house")
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
				{this.state.data.map(house => {
					return (
						<li key={house.id}>
							{house.name}
						</li>
					);
				})}
			</ul>
		);
	}
}

export default House_info;