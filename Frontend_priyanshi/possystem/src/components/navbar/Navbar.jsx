import "./navbar.css"
import SearchIcon from '@mui/icons-material/Search';
import LanguageIcon from '@mui/icons-material/Language';
import DarkModeIcon from '@mui/icons-material/DarkMode';
import FullscreenIcon from '@mui/icons-material/Fullscreen';
import NotificationsIcon from '@mui/icons-material/Notifications';
import ChatIcon from '@mui/icons-material/Chat';
import FormatListBulletedIcon from '@mui/icons-material/FormatListBulleted';

const Navbar = () => {
  return (
    
      <div className="navbar">
        <div className="wrapper">
          <div className="search">
            <input type="text" placeholder="Search"/>
            <SearchIcon className="icon"/>
          </div>
          <div className="items">
            <div className="item">
              <LanguageIcon className="icon"/>
              English
            </div>
            <div className="item">
              <DarkModeIcon className="icon"/>
            </div>
            <div className="item">
              <FullscreenIcon className="icon"/>
            </div>
            <div className="item">
              <NotificationsIcon className="icon"/>
              <div className="counter">1</div>
            </div>
            <div className="item">
              <ChatIcon className="icon"/>
              <div className="counter">2</div>
            </div>
            <div className="item">
              <FormatListBulletedIcon className="icon"/>
            </div>
            <div className="item">
              <img src="" alt="" className="avatar"/>
            </div>
          </div>
        </div>
          
      </div>
    
  )
}

export default Navbar