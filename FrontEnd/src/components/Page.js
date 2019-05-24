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

class Page extends React.Component {
  constructor() {
    super();
    this.state = {
      driver_name: "",
      origin: "",
      dest: "",
      data: [],
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
    const rand = Math.floor(Math.random() * Math.floor(10000));
    console.log(this.state);
    axios.post(
      (process.env.BACKEND_URL || "http://18.215.243.105:5000") + "/entry",
      {
        personid: { rand },
        // originlatitude: this.state.originCoords[0],
        // originlongitude: this.state.originCoords[1],
        // destlatitude: this.state.destCoords[0],
        // destlongitude: this.state.destCoords[1],
        originlatitude: rand * 1,
        originlongitude: rand * 2,
        destlatitude: rand * 3,
        destlongitude: rand * 4,
        starttime: this.state.date + " " + this.state.time,
        radiusmiles: 0.5,
        type: "Uber",
        comment: "Let's go on a rideeeee"
      }
    );
  }

  componentDidMount() {
    axios
      .get(
        (process.env.REACT_APP_BACKEND_URL || "http://18.215.243.105:5000") +
          "/groups"
      )
      .then(res => {
        console.log(res);
        console.log(res.data);
        console.log(res.data.groups);
        let groups = res.data.groups;
        this.setState({ data: groups });
      });
  }

  handleMakeRide(o, d, t, da) {
    console.log(o);
    console.log(d);
    console.log(this.state.date);
    // this.setState({
    //   driver_name: prompt(
    //     "What is the name of the driver or the ride initiator?"
    //   )
    // });
    let driver_name = prompt(
      "What is the name of the driver or the ride initiator?"
    );
    console.log(this.state);
    let rand = Math.random() * Math.floor(10000);
    axios.post(
      (process.env.BACKEND_URL || "http://18.215.243.105:5000") + "/groups",
      {
        group_members: driver_name,
        // originlatitude: this.state.originCoords[0],
        // originlongitude: this.state.originCoords[1],
        // destlatitude: this.state.destCoords[0],
        // destlongitude: this.state.destCoords[1],
        originlatitude: rand * 1,
        originlongitude: rand * 2,
        destlatitude: rand * 3,
        destlongitude: rand * 4,
        starttime: this.state.date + " " + this.state.time
      }
    );
  }

  handleAddressChangeOrigin(origin) {
    console.log("HELLO");

    this.setState({ origin });
    console.log(this.state.origin);
  }

  handleCoordsChangeOrigin(coords) {
    console.log("HELLO");

    this.setState({ originCoords: [coords.lat, coords.lng] });
  }

  handleAddressChangeDest(dest) {
    console.log("HELLO");

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
          {this.state.data.map(item => (
            <Post
              name={item.group_members.split(",")[0]}
              origin={this.state.origin}
              destination={this.state.dest}
              time={item.starttime}
              originCoords={[item.originlatitude, item.originlongitude]}
              destinationCoords={[item.destlatitude, item.destlongitude]}
              key={item.group_members.split(",")[0] + item.starttime}
              passengers={item.group_members}
              onAddPass={this.handleAddPass}
            />
          ))}
        </div>
      </div>
    );
  }
}

export default Page;
