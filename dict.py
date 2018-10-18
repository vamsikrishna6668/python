d1={"Employee":
        {"Developer":
             {"Morning":{"101":{"name":"Ismail","cno":8500580},
                         "102":{"name":"anji","cno":81254694}
                        },
             "Evening":{"103":{"name":"chanti","cno":784589756},
                         "104":{"name":"sathi","cno":95503811}
                        },
             },

        "Tester":
             {"Morning":{"105":{"name":"harsha","cno":8945756985},
                         "106":{"name":"Rakesh","cno":5649954755}
                        },
             "Evening":{"107":{"name":"sai Teja","cno":8754885545},
                        "108":{"name":"balaram","cno":9845785545}
                       },
             },
        "Desginer":
             {"Morning":{"109":{"name":"Rajesh","cno":897554566},
                         "110":{"name":"vamsi","cno":880183518}
                        },
             "Evening":{"111":{"name":"kiran","cno":93939355},
                        "112":{"name":"kishore","cno":90102434}
                       }
             }

        }
   }

#print(d1)
#print(d1["Employee"])
#print(d1["Employee"]["Developer"])
#print(d1["Employee"]["Developer"]["Morning"])
#print(d1["Employee"]["Developer"]["Morning"])
#print(d1["Employee"]["Desginer"]["Morning"])
print(d1["Employee"]["Tester"]["Evening"])