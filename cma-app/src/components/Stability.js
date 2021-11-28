// transactions by month
// -> investment rrsp etf stocks 
// -> savings house car emergency shopping hobby travel 
//    -> categorized 
// -> expenses
//    -> categorized
import React, { useState, useEffect } from "react";
import DateFnsUtils from '@date-io/date-fns';
import { DatePicker, MuiPickersUtilsProvider } from "@material-ui/pickers";
import { Grid } from "@material-ui/core";
import { makeStyles } from '@material-ui/core/styles';
import { getAllTransactions } from '../api'
import Transactions from './Transactions'

const useStyles = makeStyles((theme) => ({
  root: {
    flexGrow: 4,
    height: '100%',
    width: '100%'
  }
}));

function Stability() {
    const [selectedDate, setSelectedDate] = useState(new Date());
    const [transactions, setTransactions] = useState([]);
    const classes = useStyles();

    useEffect(() => {
        const month = selectedDate.getMonth()
        const year = selectedDate.getFullYear()
        getAllTransactions(month, year).then(res => { 
            console.log(res)
            setTransactions(res);
        })
    }, [selectedDate])

    return (
        <div className={classes.root}>
            <Grid
            container
            direction="column"
            justifyContent="space-between">
                <Grid item>
                    <Grid container>
                        <MuiPickersUtilsProvider utils={DateFnsUtils}>
                            <DatePicker
                            variant="inline"
                            openTo="year"
                            views={["year", "month"]}
                            label="Year and Month"
                            helperText="Start from year selection"
                            value={selectedDate}
                            onChange={setSelectedDate}
                            />
                        </MuiPickersUtilsProvider>
                    </Grid>
                </Grid>
                <Transactions transactions={transactions} />
            </Grid>
        </div>
    )
    
}

export default Stability;