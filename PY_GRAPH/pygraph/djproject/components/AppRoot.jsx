import Activity from './pages/Activity';

const indexRoute = {
  component: Activity.syncComponent,
};
const App = require('./App');

module.exports = {
  path: '/',
  component: App,

  /* Main Navigation Page */
  indexRoute: indexRoute,

  getChildRoutes(location, callback) {
    require.ensure([], function childRouteFunc(require) {
      callback(null, [
        // site
        require('./pages/About'),
        require('./pages/Activity'),
        require('./pages/Members'),
        // user
        require('./pages/Login'),
        require('./pages/Logout'),
        require('./pages/Profile'),
        require('./pages/Signup'),
        // admin
        require('./pages/Dashboard'),
        //  404
        // require("../pages/NotFound")

      ]);
    });
  },
};