import React from 'react';
import { Route, IndexRoute } from 'react-router';

/* Containers BEGIN */
import Xpansiv from './index';
import Home from './screens/Home';
import Login from './screens/Login';
import SignUp from './screens/SignUp';
import Production from './screens/Production/screens/All';
import ProductionDetail from './screens/Production/screens/Detail';
import WellPadsDetail from './screens/Production/screens/WellPads';
import Buyers from './screens/Buyers/screens/All';
import BuyerDetail from './screens/Buyers/screens/Detail';
import Standards from './screens/Standards/screens/All';
import StandardDetail from './screens/Standards/screens/Detail';
import CIFs from './screens/CIFs/screens/All';
import CIFDetail from './screens/CIFs/screens/Detail';

/* Containers END */

export const routes = (store, dispatch) => {
  return (
    <Route path='xpansiv'>
      <Route component={Xpansiv}>
        <IndexRoute component={Home} />
        <Route path='home' component={Home}/>
        <Route path='production'>
          <IndexRoute component={Production} />
          <Route path=':id' component={ProductionDetail} />
          <Route path='wellpads/:id' component={WellPadsDetail} />
        </Route>
        <Route path='buyers'>
          <IndexRoute component={Buyers} />
          <Route path=':id' component={BuyerDetail} />
        </Route>
        <Route path='standards'>
          <IndexRoute component={Standards} />
          <Route path=':id' component={StandardDetail} />
        </Route>
        <Route path='cifs'>
          <IndexRoute component={CIFs} />
          <Route path=':id' component={CIFDetail} />
        </Route>
      </Route>
       <Route path='login' component={Login}/>
       <Route path='signup' component={SignUp}/>
    </Route>
  );
};
