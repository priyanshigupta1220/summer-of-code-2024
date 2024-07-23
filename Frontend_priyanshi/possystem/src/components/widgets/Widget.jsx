import "./widget.css"
import ArrowDropUpIcon from '@mui/icons-material/ArrowDropUp';
import PersonIcon from '@mui/icons-material/Person';
import ShoppingCartIcon from '@mui/icons-material/ShoppingCart';
import CurrencyRupeeIcon from '@mui/icons-material/CurrencyRupee';
import AccountBalanceWalletIcon from '@mui/icons-material/AccountBalanceWallet';
import { colors } from "@mui/material";
import { green } from "@mui/material/colors";

const Widget = ({type}) => {
  let data;  

  //temporary
  const amount=100;
  const diff=20;
    switch(type){
        case "user":
            data={
                title:"USERS",
                isMoney:false,
                link:"View all users",
                icon:(<PersonIcon className="icon" style={{backgroundColor:"rgb(255,0,0,0.2)",color:"red"}}/>),
            };
            break;
        case "order":
            data={
                title:"ORDERS",
                isMoney:false,
                link:"View all orders",
                icon:(<ShoppingCartIcon className="icon" style={{backgroundColor:"rgb(218,165,32,0.2)",color:"goldenrod"}}/>),
            };
            break;

        case "earnings":
            data={
                title:"EARNINGS",
                isMoney:true,
                link:"View net earnings",
                icon:(<CurrencyRupeeIcon className="icon" style={{backgroundColor:"rgb(0,128,0,0.2)",color:"green"}}/>),
            };
            break;
        
        case "balance":
            data={
                title:"BALANCE",
                isMoney:true,
                link:"See details",
                icon:(<AccountBalanceWalletIcon className="icon" style={{backgroundColor:"rgb(128,0,128,0.2)",color:"purple"}}/>),
            };
            break;

        default:
            break;
    }
  return (
    <div className="widget">
        <div className="left">
            <span className="title">{data.title}</span>
            <span className="counter">{data.isMoney && "₹"}{amount}</span>
            <span className="link">{data.link}</span>
        </div>
        <div className="right">
            <div className="percentage positive">
            <ArrowDropUpIcon/>{diff}%
            </div>
            {data.icon}

        </div>
    </div>
  )
}

export default Widget