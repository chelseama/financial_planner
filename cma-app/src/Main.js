// what do I want to display
// credit card, chequing, questrade, wealthsimple

import React from 'react';
import './Main.css'
import Health from './components/Health'
import Stability from './components/Stability'
import Experience from './components/Experience'
import { Tabs, Tab, Typography, Box, AppBar, Grid } from '@material-ui/core';
import SwipeableViews from 'react-swipeable-views';


function TabPanel(props) {
  const { children, value, index, ...other } = props;
  return (
    <div
      role="tabpanel"
      hidden={value !== index}
      id={`full-width-tabpanel-${index}`}
      aria-labelledby={`full-width-tab-${index}`}
      {...other}
    >
      {value === index && (
        <Box p={3}>
          {children}
        </Box>
      )}
    </div>
  );
}

function a11yProps(index) {
  return {
    id: `full-width-tab-${index}`,
    'aria-controls': `full-width-tabpanel-${index}`,
  };
}

function Main() {
  const [showDirections, setShowDirections] = React.useState(0)
  const handleChange = (event, newDirections) => {
    setShowDirections(newDirections);
  };

  const handleChangeIndex = (index) => {
    setShowDirections(index);
  };
  return (

    <Grid
      container
      direction="column"
      >
      <Grid container><Typography variant="h1" className='title'>Daydreaming</Typography></Grid>
      <Grid>
        <AppBar position="static" color="default">
        <Tabs
          value={showDirections}
          onChange={handleChange}
          indicatorColor="primary"
          textColor="primary"
          variant="fullWidth"
          aria-label="full width tabs example">
          <Tab label="Health" {...a11yProps(0)} />
          <Tab label="Stability" {...a11yProps(1)} />
          <Tab label="Experience" {...a11yProps(2)} />
        </Tabs>
        </AppBar>
        <SwipeableViews
          axis={showDirections === 'rtl' ? 'x-reverse' : 'x'}
          index={showDirections}
          onChangeIndex={handleChangeIndex}>
          <TabPanel value={showDirections} index={0}> 
            <Health/>
          </TabPanel>
          <TabPanel value={showDirections} index={1}>
            <Stability/>
          </TabPanel>
          <TabPanel value={showDirections} index={2}>
            <Experience/>
          </TabPanel>
        </SwipeableViews>
      </Grid>
    </Grid>

  );
}

export default Main;
