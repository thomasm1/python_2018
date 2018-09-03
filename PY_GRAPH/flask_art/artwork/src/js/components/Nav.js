var React = require('react');
var NavLink = require('react-router-dom').NavLink;


function Nav(){
	return(
		<div id="menu-box" className="clearfix">
          	<nav id="site-navigation" className="main-navigation clearfix">
				<ul id='menu-dash2menu' className='nav'>
					<li>
						<NavLink exact activeClassName='current-menu-item' to="/index.php/moms-organic-grocery">
							Overview
						</NavLink>
					</li>
					<li>
						<NavLink exact activeClassName='current-menu-item' to="/index.php/moms-organic-grocery/portfolio">
							Portfolio
						</NavLink>
					</li>
					<li>
						<NavLink exact activeClassName='current-menu-item' to="/index.php/moms-organic-grocery/pending">
							Pending Contracts
						</NavLink>
					</li>
				</ul>
		    </nav>
        </div>	
		)
}

export default Nav;