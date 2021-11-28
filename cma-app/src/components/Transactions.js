import { Grid } from "@material-ui/core";
import { DataGrid } from '@material-ui/data-grid';

const Transactions = t => {
    console.log(t)
    const {total, plus, minus, transactions} = t.transactions
    console.log("t", total, transactions)
    if (transactions && transactions.length>0) {
        for (var i=0; i<transactions.length; i++) {
            transactions[i]['id'] = i
        }
        return (
            <div>
                <Grid item>
                    <Grid container>
                        <div style={{ height: 300, width: '100%' }}>
                        <DataGrid
                        columns={[{ field: 'category', width: 150 }, { field: 'date', width: 150  },{ field: 'name', width: 500  },{ field: 'price', width: 150  }]}
                        rows={transactions}
                        />
                        </div>
                    </Grid>
                </Grid>
                <Grid item>Total is: {total}</Grid>
                <Grid item>Total Spending is: {minus}</Grid>
                <Grid item>Total Earning is: {plus}</Grid>
            </div>
        )
    } else {
        return <div></div>
    }  
}

export default Transactions;