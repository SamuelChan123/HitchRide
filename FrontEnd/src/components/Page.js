import React from "react";

import Post from "./Post";
import Header from "./Header";

const styles = {
  postContainer: {
    display: "flex",
    justifyContent: "center",
    alignItems: "center",
    flexDirection: "column"
  }
};

const data = [
  {
    name: "Josh Kennedy",
    origin: "1717 Office",
    destination: "Omni Hotel",
    time: "May 25 at 1:00pm",
    originCoords: [52.505, -0.09],
    destinationCoords: [52.555, -0.09]
  },
  {
    name: "Benny Beinish",
    origin: "Omni Hotel",
    destination: "Richmond Airport",
    time: "May 24 at 3:00pm",
    originCoords: [51.505, -0.09],
    destinationCoords: [51.555, -0.09]
  },
  {
    name: "Samarth Kishor",
    origin: "1717 Office",
    destination: "A tall cliff",
    time: "May 25 at 5:00am",
    originCoords: [51.505, -1.09],
    destinationCoords: [51.555, -1.09]
  }
];

class Page extends React.Component {
  constructor() {
    super();
    this.state = {origin: "", dest: "", date: null, time: null};
    this.handleSearch = this.handleSearch.bind(this);
    this.handleAddressChangeOrigin = this.handleAddressChangeOrigin.bind(this);
    this.handleAddressChangeDest = this.handleAddressChangeDest.bind(this);
    this.handleDateChange = this.handleDateChange.bind(this);
    this.handleTimeChange = this.handleTimeChange.bind(this);
  }

  handleSearch() {
    alert(this.state.time);
  }

  handleAddressChangeOrigin(origin) {
    this.setState({ origin });
  }

  handleAddressChangeDest(dest) {
    this.setState({ dest });
  }

  handleDateChange(event) {
    this.setState({date: event});
  }

  handleTimeChange(time) {
    this.setState({time: time});
  }


  render() {
    return (
      <div>
        <Header 
        onSearch={this.handleSearch}
        onAddressChangeOrigin={this.handleAddressChangeOrigin}
        onAddressChangeDest={this.handleAddressChangeDest}
        onDateChange={this.handleDateChange}
        onTimeChange={this.handleTimeChange}

        />
        <div style={styles.postContainer}>
          {data.map(item => (
            <Post
              name={item.name}
              origin={item.origin}
              destination={item.destination}
              time={item.time}
              originCoords={item.originCoords}
              destinationCoords={item.destinationCoords}
              key={item.name + item.time}
            />
          ))}
        </div>
      </div>
    );
  }
}

export default Page;
