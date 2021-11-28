
import React, { useState } from "react";
import { Typography, Checkbox, Paper, List, ListItem, ListItemText, Grid } from "@material-ui/core";

// routine
function Health() {
    const [state, setState] = useState({
        checked1: true,
        checked2: true,
        checked3: true,
        checked4: true,
        checked5: true,
        checked6: true,
        checked7: true,
        checked8: true,
    });

    const handleChange = (event) => {
        setState({ ...state, [event.target.name]: event.target.checked });
    };

    return (
        <div>
            <Grid
                container
                direction="column"
                justifyContent="space-between">
                <Grid item>
                    <Grid container>
                        <Paper>
                            <Typography variant="h4">Healthy Habits</Typography>
                            <List>
                                <ListItem>
                                    <Checkbox
                                        checked={state.checked1}
                                        onChange={handleChange}
                                        name="checked1"
                                        color="primary" />
                                    <ListItemText primary="Wake up at sunrise" />
                                </ListItem>

                                <ListItem>
                                    <Checkbox
                                        checked={state.checked2}
                                        onChange={handleChange}
                                        name="checked2"
                                        color="primary" />
                                    <ListItemText primary="Work Out" />
                                </ListItem>

                                <ListItem>
                                    <Checkbox
                                        checked={state.checked3}
                                        onChange={handleChange}
                                        name="checked3"
                                        color="primary" />
                                    <ListItemText primary="Journal" />
                                </ListItem>

                                <ListItem>
                                    <Checkbox
                                        checked={state.checked4}
                                        onChange={handleChange}
                                        name="checked4"
                                        color="primary" />
                                    <ListItemText primary="Meditate" />
                                </ListItem>

                                <ListItem>
                                    <Checkbox
                                        checked={state.checked5}
                                        onChange={handleChange}
                                        name="checked5"
                                        color="primary" />
                                    <ListItemText primary="Read books" />
                                </ListItem>

                                <ListItem>
                                    <Checkbox
                                        checked={state.checked6}
                                        onChange={handleChange}
                                        name="checked6"
                                        color="primary" />
                                    <ListItemText primary="Learn something new" />
                                </ListItem>

                                <ListItem>
                                    <Checkbox
                                        checked={state.checked4}
                                        onChange={handleChange}
                                        name="checked7"
                                        color="primary" />
                                    <ListItemText primary="Go for a walk" />
                                </ListItem>

                                <ListItem>
                                    <Checkbox
                                        checked={state.checked7}
                                        onChange={handleChange}
                                        name="checked8"
                                        color="primary" />
                                    <ListItemText primary="Sleep 8hrs before sunrise" />
                                </ListItem>
                            </List>
                        </Paper>
                    </Grid>
                </Grid>
                {/* <Grid item>
                    <Grid container>
                        <Paper>
                            <Typography variant="h4">Healthy Budget</Typography>
                            <List>
                                <ListItem>
                                    <ListItemText primary="Home: 2000" />
                                </ListItem>
                                <ListItem>
                                    <ListItemText primary="Utilities: 200" />
                                </ListItem>
                                <ListItem>
                                    <ListItemText primary="Food and Drink: 500" />
                                </ListItem>
                                <ListItem>
                                    <ListItemText primary="Transportation: 450" />
                                </ListItem>
                            </List>
                        </Paper>
                    </Grid>
                </Grid> */}
            </Grid>
        </div>
    )
}

export default Health;