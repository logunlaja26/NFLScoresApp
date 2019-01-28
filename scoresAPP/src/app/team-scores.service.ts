import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { HttpClient } from '@angular/common/http';



@Injectable({
  providedIn: 'root'
})
export class TeamScoresService {

  constructor(private httpClient: HttpClient) { }

  getTeamScores(): Observable<any>{
    let eachTeamScores = this.httpClient.get("/api/teams");
    console.log('team_scores', eachTeamScores)
    return eachTeamScores;
  }

  getColumns(): string[] {
  	return ["Team","Average Points Scored","Average Points Allowed"]};

}
