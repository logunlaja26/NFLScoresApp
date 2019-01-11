import { Component, OnInit } from '@angular/core';
import { TeamScoresService } from '../team-scores.service';
import { Observable } from 'rxjs';


@Component({
  selector: 'app-teams',
  templateUrl: './teams.component.html',
  styleUrls: ['./teams.component.css']
})
export class TeamsComponent implements OnInit {
  teamsData: Observable<any[]>;
  columns: string[];

  constructor(private teamScores: TeamScoresService) { }

  ngOnInit() {
    this.columns = this.teamScores.getColumns();

    this.teamsData = this.teamScores.getTeamScores();
  }

}
