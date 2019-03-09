import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import {ErrorPageComponent} from './shared/error-page/error-page.component';
import {SuccessComponent} from './shared/success/success.component';
import {HomeComponent} from './home/home.component';
import { PollComponent } from './poll/poll.component';

const routes: Routes = [
  {
    path: 'anketa',
    component: PollComponent
  },
  {
    path: 'success',
    component: SuccessComponent
  },
  {
    path: '',
    component: PollComponent
  },
  {
    path: '**',
    component: ErrorPageComponent
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
