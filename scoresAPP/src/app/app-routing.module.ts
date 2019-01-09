import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { HistoryComponent } from './history/history.component';
import { HomeComponent } from './home/home.component';
import { TeamsComponent } from './teams/teams.component';

const routes: Routes = [
 {path: '', component: HomeComponent },
 {path: 'home', component: HomeComponent },
 {path: 'history', component: HistoryComponent },
 {path: 'teams', component: TeamsComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
