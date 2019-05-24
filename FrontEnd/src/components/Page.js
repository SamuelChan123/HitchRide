import React from "react";
import axios from "axios";

import Post from "./Post";
import Header from "./Header";

require("dotenv").config();

const styles = {
  postContainer: {
    display: "flex",
    justifyContent: "center",
    alignItems: "center",
    flexDirection: "column"
  }
};

let data = [];

class Page extends React.Component {
  constructor() {
    super();
    this.state = {
      origin: "",
      dest: "",
      date: null,
      time: null,
      originCoords: [],
      destCoords: []
    };
    this.handleSearch = this.handleSearch.bind(this);
    this.handleAddressChangeOrigin = this.handleAddressChangeOrigin.bind(this);
    this.handleCoordsChangeOrigin = this.handleCoordsChangeOrigin.bind(this);
    this.handleAddressChangeDest = this.handleAddressChangeDest.bind(this);
    this.handleCoordsChangeDest = this.handleCoordsChangeDest.bind(this);
    this.handleDateChange = this.handleDateChange.bind(this);
    this.handleTimeChange = this.handleTimeChange.bind(this);
    this.handleMakeRide = this.handleMakeRide.bind(this);
    this.handleAddPass = this.handleAddPass.bind(this);
  }

  handleSearch() {
    console.log(this.state.originCoords);
    console.log(this.state.destCoords);
    axios.post((process.env.BACKEND_URL || 'http://localhost:5000') + "/entry", {
      personId: 1,
      originlatitude: this.state.originCoords[0],
      originlongitude: this.state.originCoords[1],
      destinationlatitude: this.state.destCoords[0],
      destinationlongitude: this.state.destCoords[1],
      starttime: this.state.date + " " + this.state.time,
      radiusmiles: 0.5,
      type: "Uber",
      comment: "Let's go on a rideeeee"
    });
  }

  handleMakeRide() {
    console.log(this.state.originCoords);
    console.log(this.state.date);
    this.setState({driver_name: prompt("What is the name of the driver or the ride initiator?")});
    axios.post((process.env.BACKEND_URL || 'http://localhost:5000') + "/groups", {
      group_members: this.state.driver_name,
      originlatitude: this.state.originCoords[0],
      originlongitude: this.state.originCoords[1],
      destlatitude: this.state.destCoords[0],
      destlongitude: this.state.destCoords[1],
      starttime: this.state.date + " " + this.state.time,
      radiusmiles: 0.5,
      type: "Uber",
      comment: "I would love a ride to these locations!"
    });
  }

  handleAddressChangeOrigin(origin) {
    this.setState({ origin });
  }

  handleCoordsChangeOrigin(coords) {
    this.setState({ originCoords: [coords.lat, coords.lng] });
  }

  handleAddressChangeDest(dest) {
    this.setState({ dest });
  }

  handleCoordsChangeDest(coords) {
    this.setState({ destCoords: [coords.lat, coords.lng] });
  }

  handleDateChange(event) {
    this.setState({ date: event });
  }

  handleTimeChange(time) {
    this.setState({ time: time });
  }

  handleAddPass(passengers) {
    //passengers is the recently added p

  }

  render() {


    axios.get((process.env.REACT_APP_BACKEND_URL || 'http://localhost:5000') + '/groups').then(res => {
      this.setState(res);
    });

    return (
      <div>
        <Header
          onSearch={this.handleSearch}
          onAddressChangeOrigin={this.handleAddressChangeOrigin}
          onAddressChangeDest={this.handleAddressChangeDest}
          onCoordsChangeOrigin={this.handleCoordsChangeOrigin}
          onCoordsChangeDest={this.handleCoordsChangeDest}
          onDateChange={this.handleDateChange}
          onTimeChange={this.handleTimeChange}
          makeRide={this.handleMakeRide}
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
              passengers={item.passengers}
              onAddPass={this.handleAddPass}
            />
          ))}
        </div>
      </div>
    );
  }
}

export default Page;
