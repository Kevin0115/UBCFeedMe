import { Component, OnInit } from '@angular/core';
import {PostsService} from "../posts.service";

@Component({
  selector: 'app-posts',
  templateUrl: './posts.component.html',
  styleUrls: ['./posts.component.css']
})
export class PostsComponent implements OnInit {
  posts: Array<Post> = [];

  constructor(private postsService: PostsService) { }

  /**
   * Load posts from the server and deserialize the response
   */
  ngOnInit() {
    this.postsService.getAllPosts().subscribe(res => {
      this.posts = res.map(entry => {
        return new Post(
          entry._id,
          entry.event,
          entry.organization,
          entry.date,
          entry.location,
          entry.url,
          parseTime(entry.start_time),
          parseTime(entry.end_time),
          parseInt( (entry.date.trim()).concat( entry.start_time.trim() ).split('-').join('').split(':').join(''))
        );
      });
      this.posts.sort(function(a, b) {
        return a.dateInt - b.dateInt;
      });
    })


  }
}

//I am so disgusted by what I have created
function parseTime(time){
  var timeInt = parseInt( time.trim().slice(0,5).split(':').join('') );
  var isAm = true;

  if(timeInt >= 1299){
    timeInt -= 1200;
    isAm = false;
  }

  var timeString =  timeInt + '';
  var colonPosition = 1;

  if(timeInt > 999) {
    colonPosition = 2;
  }
  if(isAm) {
    return timeString.slice(0, colonPosition) + ":" + timeString.slice(colonPosition) + "am";
  }
  else{
    return timeString.slice(0, colonPosition) + ":" + timeString.slice(colonPosition) + "pm";
  }
}
export class Post {
  constructor(
    public id: string,
    public eventName: string,
    public org: string,
    public date: string,
    public location: string,
    public url: string,
    public startTime: string,
    public endTime: string,
    public dateInt: number,
  ) { }
}
