import { Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';
import { TEAM_SCORES } from './teamScores-data';
import { HttpClient } from '@angular/common/http';



@Injectable({
  providedIn: 'root'
})
export class TeamScoresService {

  constructor() { }

  getTeamScores(): Observable<any>{
    console.log('team_scores',TEAM_SCORES)
    return of(TEAM_SCORES);
  }

  getColumns(): string[] {
  	return ["Team","Wins","Losses","Average Points Scored","Average Points Allowed","Average Points Differential"]};

}
