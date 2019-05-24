import React from "react";
import PropTypes from "prop-types";
import axios from "axios";

import { withStyles } from "@material-ui/core/styles";
import Card from "@material-ui/core/Card";
import Dialog from "@material-ui/core/Dialog";
import CardHeader from "@material-ui/core/CardHeader";
import CardContent from "@material-ui/core/CardContent";
import Avatar from "@material-ui/core/Avatar";
import Typography from "@material-ui/core/Typography";
import Button from "@material-ui/core/Button";

import PostMap from "./PostMap";

const styles = theme => ({
  card: {
    width: 800,
    height: 200,
    margin: "10px",
    display: "flex",
    flexDirection: "row",
    justifyContent: "space-between",
    alignItems: "center"
  }
});

class Post extends React.Component {
  constructor(props) {
    super(props);
    this.state = { passengers: [] };
    this.handleClick = this.handleClick.bind(this);
  }

  handleClick() {
    let passengers = [...this.state.passengers];
    passengers.push(
      prompt(
        "Before you accept this be 100% sure that you want to participate in this ride. Enter your name below and press enter."
      )
    );

    this.setState({ passengers });
    this.props.onAddPass(passengers);

    axios.post(
      (process.env.BACKEND_URL || "http://localhost:5000") + "/groups/",
      {
        personId: 1,
        origin: this.state.originCoords[0],
        destination: this.state.destCoords[1],
        starttime: this.state.date + " " + this.state.time,
        endtime: this.state.date + " " + this.state.time,
        radiusmiles: 0,
        type: "Uber",
        comment: "yeet"
      }
    );
  }

  render() {
    const { classes } = this.props;
    return (
      <div>
        <Card className={classes.card}>
          <div>
            <CardHeader
              avatar={
                <Avatar aria-label="Name">
                  {this.props.name[0] +
                    this.props.name
                      .trim()
                      .split(" ")
                      .slice(-1)[0][0]
                      .toUpperCase()}
                </Avatar>
              }
              title={this.props.name}
              subheader={this.props.time}
            />
            <CardContent>
              <Typography paragraph>Origin: {this.props.origin}</Typography>
              <Typography paragraph>
                Destination: {this.props.destination}
              </Typography>
              <Typography paragraph>
                Passengers: {this.state.passengers.join(", ")}
              </Typography>
            </CardContent>
          </div>
          <div>
            <Button
              variant="contained"
              color="primary"
              size="large"
              onClick={this.handleClick}
            >
              Join
            </Button>
          </div>
          <div id="map-container">
            <PostMap
              origin={this.props.origin}
              destination={this.props.destination}
              originCoords={this.props.originCoords}
              destinationCoords={this.props.destinationCoords}
            />
          </div>
        </Card>
      </div>
    );
  }
}

Post.propTypes = {
  classes: PropTypes.object.isRequired
};

export default withStyles(styles)(Post);
