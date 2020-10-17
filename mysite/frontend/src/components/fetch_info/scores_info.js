import React, { Component } from "react";
import { render } from "react-dom";

class Scores_info extends Component {
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
		fetch("bounty/api/scores")
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
				{this.state.data.map(score => {
					return (
						<li key={score.id}>
							{score.topic} - {score.score}
						</li>
					);
				})}
			</ul>
		);
	}
}

export default Scores_info;