import "./sidebar.css";
import SpaceDashboardIcon from '@mui/icons-material/SpaceDashboard';
import InventoryIcon from '@mui/icons-material/Inventory';
import AnalyticsIcon from '@mui/icons-material/Analytics';
import NotificationsIcon from '@mui/icons-material/Notifications';
import PersonIcon from '@mui/icons-material/Person';
import SettingsIcon from '@mui/icons-material/Settings';
import GroupIcon from '@mui/icons-material/Group';
import ReceiptLongIcon from '@mui/icons-material/ReceiptLong';
import AccountCircleIcon from '@mui/icons-material/AccountCircle';
import LogoutIcon from '@mui/icons-material/Logout';
const Sidebar = () => {
  return (
    <div className="sidebar">
        <div className="top">
            <span className="logo">POS System</span>
        </div>
        <hr/>
        <div className="center">
            <ul>
                <p className="title">MAIN</p>
                <li>
                    <SpaceDashboardIcon className="icon"/>
                    <span>Dashboard</span>
                </li>
                <p className="title">LISTS</p>
                <li>
                    <GroupIcon className="icon"/>
                    <span>Staff</span>
                </li>
                <li>
                    <PersonIcon className="icon"/>
                    <span>Customers</span>
                </li>
                <li>
                    <InventoryIcon className="icon"/>
                    <span>Products</span>
                </li>
                <li>
                    <ReceiptLongIcon className="icon"/>
                    <span>Transactions</span>
                </li>
                <p className="title">USEFUL</p>
                <li>
                    <AnalyticsIcon className="icon"/>
                    <span>Analytics</span>
                </li>
                <li>
                    <NotificationsIcon className="icon"/>
                    <span>Notifications</span>
                </li>
                <li>
                    <SettingsIcon className="icon"/>
                    <span>Settings</span>
                </li>
                <p className="title">USER</p>
                <li>
                    <AccountCircleIcon className="icon"/>
                    <span>Profile</span>
                </li>
                <li>
                    <LogoutIcon className="icon"/>
                    <span>Logout</span>
                </li>
            </ul>
        </div>
        <div className="bottom">
            <div className="colorOptions"></div>
            <div className="colorOptions"></div>
        </div>
    </div>
  )
}

export default Sidebar