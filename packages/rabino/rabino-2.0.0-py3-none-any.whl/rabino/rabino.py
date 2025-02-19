from aiohttp import ClientSession
import asyncio,random,json
from pathlib import Path
from tqdm import tqdm


class rubino:
	def __init__(self, auth):
		self.auth = auth
		self.session = None
		print("rabino starts......")
		print("Creator : Mamadcoder \nid Telegram: https://t.me/RMSource")
	async def __aenter__(self):
		
		self.session = ClientSession()
		return self

	async def __aexit__(self, exc_type, exc_val, exc_tb):
		if self.session:
			await self.session.close()
		return None

	async def GET(self, url):
		if not self.session:
			raise RuntimeError("Session is not initialized")
		async with self.session.get(url) as res:
		          data = await res.text()
		          return data
	async def get_thumbnail(self,video_path, output_path, time_sec=5):
	    import cv2
	    video_path = Path(video_path)
	    output_path = Path(output_path)
	    if not video_path.exists():
	        raise FileNotFoundError(f"فایل ویدیو یافت نشد: {video_path}")
	    cap = cv2.VideoCapture(str(video_path))
	    fps = cap.get(cv2.CAP_PROP_FPS)
	    frame_number = int(fps * time_sec)
	    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number)
	    ret, frame = cap.read()
	    if ret:
	        cv2.imwrite(str(output_path), frame)
	        return open(output_path,"rb").read()
	    else:
	        raise Exception("خطا در خواندن فریم.")
	        
	async def POST_DATA(self, method:str,input:dict,auth=None) -> dict:
		
		url = f"https://rubino{random.randint(1,30)}.iranlms.ir/"
		async with self.session.post(url=url,json={"api_version": "0","auth": self.auth if not auth else auth,"client":{"app_name":"Main","app_version":"3.5.7","lang_code":"fa","package":"app.rbmain.a","temp_code":"31","platform":"Android"},"data": input,"method": method}) as res:
				data = await res.json()
				return data
	async def get_me(self,profile_id=None):
		return await self.POST_DATA("getMyProfileInfo",{ "profile_id": profile_id})
	async def follow(self,follow_id:str,profile_id:str=None) -> str:
		return await self.POST_DATA('requestFollow',{"f_type": "Follow","followee_id": follow_id,"profile_id": profile_id})
	async def post_byte(self,url,data,header):
		async with self.session.post(url=url,data=data,headers=header) as res:
			data = await res.json()
			
			return data
	
	async def request_file(self,file,Type="Picture",size=None,profile_id=None):
			return await self.POST_DATA("requestUploadFile",{"file_name": file.split("/")[-1],"file_size": size or Path(file).stat().st_size, "file_type": Type,"profile_id": profile_id})
	async def fetch_file_content(self,url):
		async with self.session.get(url) as response:
			if response.status == 200:
				content = await response.read()
				return content
			else:
				raise Exception(f"Failed to fetch file: {response.status}")
	async def upload_file(self,file,type="Picture",profile_id=None,file_name=None):
		if not "http" in file:
			if not Path(file).exists():
				raise FileNotFoundError(f"File {file} does not exist")
			RESPONS = await self.request_file(file,Type=type,profile_id=profile_id)
			bytef = open(file,"rb").read()
			
			file_id = RESPONS["data"]["file_id"]
			hash_send = RESPONS["data"]["hash_file_request"]
			url = RESPONS["data"]["server_url"]
			header = {'auth':self.auth,'Host':url.replace("https://","").replace("/UploadFile.ashx",""),'chunk-size':str(Path(file).stat().st_size),'file-id':str(file_id),'hash-file-request':hash_send,"content-type": "application/octet-stream","accept-encoding": "gzip","user-agent": "okhttp/3.12.1"}
			if len(bytef) <= 131072:
				header['part-number'],header['total-part'] = "1","1"
				j = await self.post_byte(url,data=bytef,header=header)
				return [RESPONS["data"],j['data']['hash_file_receive']]
			else:
				t = len(bytef) // 131072 + 1
				progress_bar = tqdm(total=len(bytef), unit='B', unit_scale=True, desc="Uploading")
				
				for i in range(1,t+1):
					if i != t:
						
						k = (i - 1) * 131072
						header["chunk-size"], header["part-number"], header["total-part"] = "131072", str(i),str(t)
						
						progress_bar.update(len(bytef[k:k + 131072]))
						
						while True:
							try:
								d = await self.post_byte(data=bytef[k:k + 131072],url=url,header=header)
								
								break
							except Exception as e:
								raise e
					else:
						k = (i - 1) * 131072
						header["chunk-size"], header["part-number"], header["total-part"] = str(len(bytef[k:])), str(i),str(t)
						progress_bar.update(len(bytef[k:]))
						d = await self.post_byte(url=url, data=bytef, header=header)
						
				return [RESPONS["data"],d['data']['hash_file_receive']]
		else:
			bytef = await self.fetch_file_content(file)
			REQUEST = {"file_name": file_name if file_name else file.split("/")[-1],"file_size": len(bytef), "file_type": type,"profile_id": profile_id}
			method = "requestUploadFile"
			RESPONS = await self.POST_DATA(method,REQUEST)
			
			file_id = RESPONS["data"]["file_id"]
			
			hash_send = RESPONS["data"]["hash_file_request"]
			url = RESPONS["data"]["server_url"]
			header = {'auth':self.auth,'Host':url.replace("https://","").replace("/UploadFile.ashx",""),'chunk-size':str(len(bytef)),'file-id':str(file_id),'hash-file-request':hash_send,"content-type": "application/octet-stream","accept-encoding": "gzip","user-agent": "okhttp/3.12.1"}
			if len(bytef) <= 131072:
				header['part-number'],header['total-part'] = "1","1"
				j = await self.post_byte(url,data=bytef,header=header)
				return [RESPONS["data"],j['data']['hash_file_receive']]
			else:
				t = len(bytef) // 131072 + 1
				progress_bar = tqdm(total=len(bytef), unit='B', unit_scale=True, desc="Uploading")
				
				for i in range(1,t+1):
					if i != t:
						
						k = (i - 1) * 131072
						header["chunk-size"], header["part-number"], header["total-part"] = "131072", str(i),str(t)
						
						progress_bar.update(len(bytef[k:k + 131072]))
						
						while True:
							try:
								d = await self.post_byte(data=bytef[k:k + 131072],url=url,header=header)
								
								break
							except Exception as e:
								raise e
					else:
						k = (i - 1) * 131072
						header["chunk-size"], header["part-number"], header["total-part"] = str(len(bytef[k:])), str(i),str(t)
						progress_bar.update(len(bytef[k:]))
						d = await self.post_byte(url=url, data=bytef, header=header)
						
				return [RESPONS["data"],d['data']['hash_file_receive']]
	async def add_post(self,file,text:str=None,type="Picture",profile_id=None,thumbnail=None,file_name=None):
		"""
		Type File Upload 
		# Picture 
		# Video
		"""
		data = await self.upload_file(file,type=type,file_name=file_name,profile_id=profile_id)
		
		if type == "Picture":
			hashFile = data[1]
			fileID = data[0]["file_id"]
			thumbnailID = data[0]["file_id"]
			thumbnailHash = data[1]
			input = {"caption": text, "file_id": fileID, "hash_file_receive": hashFile, "height": 800, "width": 800, "is_multi_file": False, "post_type": type, "rnd": random.randint(100000, 999999999), "thumbnail_file_id": thumbnailID, "thumbnail_hash_file_receive": thumbnailHash, "profile_id": profile_id}
			return await self.POST_DATA("addPost",input)
		elif type == "Video":
			hash = await self.upload_file("https://tgdlir1.smhdl.ir/?ui=smhdlbot&f=AgACAgQAAxkBAAJgomevnIppSv8YSnff_zCVrVq5WnfxAALnyTEb_fSAUeQAAXHtqHqn5wEAAwIAA3kAAy8E&s=30854&n=5872963282011277799_y_4.jpg&m=image/jpeg" if not thumbnail else thumbnail, type="Picture",file_name="thumbnail.jpg",profile_id=profile_id)
			input = {"caption":text,"duration":"8","file_id":data[0]["file_id"],"hash_file_receive": data[1],"height":"1410","is_multi_file":None,"post_type":"Video","rnd":random.randint(100000, 999999999),"snapshot_file_id":hash[0]["file_id"],"snapshot_hash_file_receive":hash[1],"tagged_profiles":[],"thumbnail_file_id": hash[0]["file_id"],"thumbnail_hash_file_receive": hash[1],"width":"1080","profile_id":profile_id}
			
			return await self.POST_DATA("addPost",input)
	async def get_post_by_share_link(self,link:str,profile_id:str=None):
		if link.startswith("https://rubika.ir/post/"):
			link = link.split()[0][23:]
			input = {"share_string":link,"profile_id":profile_id}
		else:
			input = {"share_string":link,"profile_id":profile_id}
		return await self.POST_DATA("getPostByShareLink",input)
	async def add_post_view_count(self,post_id:str,target_post_id:str,profile_id=None) -> str:
		return await self.POST_DATA("addPostViewCount", {"post_id":post_id,"post_profile_id":target_post_id,"profile_id":profile_id})
		
	async def get_profile_stories(self,limit:int=100,profile_id=None):
		return await self.POST_DATA("getProfileStories", {"limit": limit, "profile_id": profile_id})
		
	async def get_story_ids(self,target_profile_id,profile_id=None):
		return await self.POST_DATA("getStoryIds",{"profile_id":profile_id,"target_profile_id":target_profile_id})
	async def get_comments(self,post_id:str,post_profile_id:str,limit=100,profile_id=None,sort="FromMax",equal=False):
		return await self.POST_DATA("getComments",{"equal": equal, "limit": limit, "sort": sort, "post_id": post_id, "profile_id": profile_id, "post_profile_id": post_profile_id})
	async def get_profile_list(self,equal=False,limit=10,sort="FromMax"):
		return await self.POST_DATA("getProfileList",{"equal":equal,"limit":limit,"sort":sort})
		
	async def get_my_profile_info(self,profile_id=None):
		return await self.POST_DATA("getMyProfileInfo",{"profile_id":profile_id})
		
	async def like_post(self,post_id:str,target_post_id:str,profile_id=None):
		return await self.POST_DATA("likePostAction",{"action_type":"Like","post_id":post_id,"post_profile_id":target_post_id,"profile_id":profile_id})
	async def get_share_link(self,post_id,post_profile_id,profile_id=None):
		return await self.POST_DATA("getShareLink",{"post_id":post_id,"post_profile_id":post_profile,"profile_id":profile_id})
	async def search_username(self,username:str)-> str:
		if username.startswith("@"):
			input = {"username": username.replace("@","")}
		else:
			input = {"username": username}
		return await self.POST_DATA("isExistUsername",input)
		
	async def add_view_story(self,story_profile_id:str,story_ids:list,profile_id=None):
		return await self.POST_DATA("addViewStory",{"profile_id":profile_id,"story_ids":story_ids,"story_profile_id":story_profile_id})
	async def create_page(self,name,username,bio=None):
		return await self.POST_DATA("createPage",{"bio": bio,"name": name,"username": username})
	async def add_comment(self,text,post_id,post_profile_id,profile_id=None):
		return await self.POST_DATA("addComment",{"content": text,"post_id": post_id,"post_profile_id": post_target,"rnd":f"{random.randint(000000,999999)}" ,"profile_id":profile_id})
	async def un_like_post(self,post_id,post_profile_id,profile_id=None):
		return await self.POST_DATA("likePostAction", {"action_type":"Unlike","post_id":post_id,"post_profile_id":post_profile_id,"profile_id":profile_id})
	async def post_book_mark_action(self,post_id,post_profile_id,profile_id=None):
		return await self.POST_DATA("postBookmarkAction",{"action_type":"Bookmark","post_id":post_id,"post_profile_id":post_profile_id,"profile_id":profile_id})
