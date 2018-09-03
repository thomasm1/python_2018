import React from 'react';
import { Route, IndexRoute } from 'react-router';

/* Containers BEGIN */
import Buyer from './index';
import Home from './screens/Home';
import Login from './screens/Login';
import SignUp from './screens/SignUp';
import Marketplace from './screens/Marketplace/screens/All';
import MarketplaceDetail from './screens/Marketplace/screens/Detail';
import RetiredCIF from './screens/Marketplace/screens/Retired';
import Transactions from './screens/Transactions/screens/All';
import TransactionDetail from './screens/Transactions/screens/Detail';
import CIFs from './screens/CIFs/screens/All';
import CIFDetail from './screens/CIFs/screens/Detail';
import Certification from './screens/Certification/screens/All';
import CertificationDetail from './screens/Certification/screens/Detail';
/* Containers END */

export const routes = (store, dispatch) => {
  return (
    <Route path='buyer'>
      <Route component={Buyer}>
        <IndexRoute component={Home} />
        <Route path='home' component={Home}/>
        <Route path='marketplace'>
          <IndexRoute component={Marketplace} />
          <Route path='retired' component={RetiredCIF} />
          <Route path=':id' component={MarketplaceDetail} />
        </Route>
        <Route path='transactions'>
          <IndexRoute component={Transactions} />
          <Route path=':id' component={TransactionDetail} />
        </Route>
        <Route path='certifications'>
          <IndexRoute component={Certification} />
          <Route path=':id' component={CertificationDetail} />
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
