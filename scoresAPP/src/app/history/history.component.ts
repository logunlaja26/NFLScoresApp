import { Component, OnInit } from '@angular/core';
import { NflScoresService } from '../nfl-scores.service'
import { Observable } from 'rxjs';

@Component({
  selector: 'app-history',
  templateUrl: './history.component.html',
  styleUrls: ['./history.component.css']
})
export class HistoryComponent implements OnInit {
  scores: Observable<any[]>;
  columns: string[];


  constructor(private nflService: NflScoresService) { }

  ngOnInit() {
  	this.columns = this.nflService.getColumns();
  	//["Date of Contest","Home team","Away team","Home team scores","Away team scores"]

  	this.scores = this.nflService.getNFLScores();
  	//all data in mock-data.ts
  }

}
