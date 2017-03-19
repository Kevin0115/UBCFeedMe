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
          entry.start_time,
          entry.end_time
        );
      });
    })
  }
}

class Post {
  constructor(
    public id: string,
    public eventName: string,
    public org: string,
    public date: string,
    public location: string,
    public url: string,
    public startTime: string,
    public endTime: string
  ) { }
}
