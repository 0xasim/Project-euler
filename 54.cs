using System;
using System.Diagnostics;
using System.Numerics;
using System.IO;

namespace euler {
    class Problem54 {
        enum Suit { Heart, Spade, Club, Diamond };
             
        Card[] hand1 = new Card[5];
        Card[] hand2 = new Card[5];
        string filename = Environment.GetFolderPath(Environment.SpecialFolder.DesktopDirectory) + "\\input.txt";
        StreamReader reader;

        public static void Main(string[] args) {
            new Problem54().BruteForce();
        }


        public void BruteForce() {
            Stopwatch clock = Stopwatch.StartNew();
            int result = 0;

            while (readHands()) {
                Array.Sort(hand1);
                Array.Sort(hand2);
                if (DidPlayer1Win(hand1, hand2)) result++;                
            }
            
            clock.Stop();
            Console.WriteLine("Player 1 won {0} hands", result);
            Console.WriteLine("Solution took {0} ms", clock.ElapsedMilliseconds);
        }


        private bool DidPlayer1Win(Card[] hand1, Card[] hand2) {
            if (IsRoyalFlush(hand1) != IsRoyalFlush(hand2)) return IsRoyalFlush(hand1) > IsRoyalFlush(hand2);            
            if (IsStraightFlush(hand1) != IsStraightFlush(hand2)) return IsStraightFlush(hand1) > IsStraightFlush(hand2);                        
            if (IsFourOfAKind(hand1) != IsFourOfAKind(hand2)) return IsFourOfAKind(hand1) > IsFourOfAKind(hand2);                        
            if (IsFullHouse(hand1, 1) != IsFullHouse(hand2, 1)) return IsFullHouse(hand1,1) > IsFullHouse(hand2,1);            
            if (IsFullHouse(hand1,2) != IsFullHouse(hand2,2)) return IsFullHouse(hand1,2) < IsFullHouse(hand2,2);                                      
            if (IsFlush(hand1) != IsFlush(hand2)) return IsFlush(hand1) > IsFlush(hand2);            
            if (IsStraight(hand1) != IsStraight(hand2)) return IsStraight(hand1) > IsStraight(hand2);                      
            if (IsThreeOfAKind(hand1) != IsThreeOfAKind(hand2)) return IsThreeOfAKind(hand1) > IsThreeOfAKind(hand2);            
            if (IsTwoPairs(hand1, 1) != IsTwoPairs(hand2, 1)) return IsTwoPairs(hand1, 1) > IsTwoPairs(hand2, 1);            
            if (IsTwoPairs(hand1, 2) != IsTwoPairs(hand2, 2)) return IsTwoPairs(hand1, 2) > IsTwoPairs(hand2, 2);            
            if (IsOnePair(hand1) != IsOnePair(hand2)) return IsOnePair(hand1) > IsOnePair(hand2);            
            if (IsHighCard(hand1,0) != IsHighCard(hand2,0)) return IsHighCard(hand1,0) > IsHighCard(hand2,0);            
            if (IsHighCard(hand1,1) != IsHighCard(hand2,1)) return IsHighCard(hand1,1) > IsHighCard(hand2,1);            
            if (IsHighCard(hand1,2) != IsHighCard(hand2,2)) return IsHighCard(hand1,2) > IsHighCard(hand2,2);            
            if (IsHighCard(hand1,3) != IsHighCard(hand2,3)) return IsHighCard(hand1,3) > IsHighCard(hand2,3);    

            return false;
        }
        
        private static int IsStraight(Card[] h) {                                               
            for (int i = 0; i < 4; i++) {
                if (h[i].Value != h[i + 1].Value - 1) {
                    return -1;                    
                }
            }
            return h[4].Value;
        }

        private static int IsFlush(Card[] h) {
            for (int i = 0; i < 4; i++) {
                if (h[i].Suit != h[i + 1].Suit) {
                    return -1;                    
                }
            }
            return h[4].Value;
        }

        private static int IsStraightFlush(Card[] h) {
            if (IsFlush(h) > 0 && IsStraight(h) > 0) {
                return h[4].Value;
            }
            return -1;                     
        }

        private static int IsRoyalFlush(Card[] h) {
            if (IsFlush(h) == 14) return 14;
            return -1;
        }

        private static int IsFourOfAKind(Card[] h) {
            if (h[0].Value == h[1].Value &&
                h[1].Value == h[2].Value &&
                h[2].Value == h[3].Value)
                return h[0].Value;
            if (h[1].Value == h[2].Value &&
                h[2].Value == h[3].Value &&
                h[3].Value == h[4].Value)
                return h[1].Value;

            return -1;

        }

        private static int IsFullHouse(Card[] h, int set) {            
            if(set == 1 &&
               h[0].Value == h[1].Value &&
               h[1].Value == h[2].Value &&
               h[3].Value == h[4].Value)
                return h[0].Value;
            if (set == 2 &&
                h[0].Value == h[1].Value &&
               h[1].Value == h[2].Value &&
               h[3].Value == h[4].Value)
                return h[4].Value;
            if(set == 1 &&
               h[0].Value == h[1].Value &&
               h[2].Value == h[3].Value &&
               h[3].Value == h[4].Value)
                return h[4].Value;
            if (set == 2 &&
                h[0].Value == h[1].Value &&
               h[2].Value == h[3].Value &&
               h[3].Value == h[4].Value)
                return h[0].Value;
            return -1;
        }

        private static int IsThreeOfAKind(Card[] h) {
            if (h[0].Value == h[1].Value &&
               h[1].Value == h[2].Value)
                return h[0].Value;

            if (h[1].Value == h[2].Value &&
               h[2].Value == h[3].Value)
                return h[1].Value;

            if (h[2].Value == h[3].Value &&
               h[3].Value == h[4].Value)
                return h[2].Value;

            return -1;
        }

        private static int IsTwoPairs(Card[] h, int set) {
            if (set == 1 &&
                h[0].Value == h[1].Value &&
                h[2].Value == h[3].Value)
                return h[0].Value;
            if (set == 2 &&
                h[0].Value == h[1].Value &&
                h[2].Value == h[3].Value)
                return h[2].Value;                        
            if (set == 1 &&
                h[0].Value == h[1].Value &&
                h[3].Value == h[4].Value)
                return h[0].Value;
            if (set == 2 &&
                h[0].Value == h[1].Value &&
                h[3].Value == h[4].Value)
                return h[3].Value;

            if (set == 1 &&
                h[1].Value == h[2].Value &&
                h[3].Value == h[4].Value)
                return h[1].Value;
            if (set == 2 &&
                h[1].Value == h[2].Value &&
                h[3].Value == h[4].Value)
                return h[3].Value;
            return -1;
        }

        private static int IsOnePair(Card[] h) {
            if (h[0].Value == h[1].Value) return h[0].Value;
            if (h[1].Value == h[2].Value) return h[1].Value;
            if (h[2].Value == h[3].Value) return h[2].Value;
            if (h[3].Value == h[4].Value) return h[3].Value;
                        
            return -1;
        }

        private static int IsHighCard(Card[] h, int card) {            
            return h[4-card].Value;
        }
        
        private bool readHands() {
            if (reader == null) reader = new StreamReader(filename);


            string line;
            string[] linePieces;
            line = reader.ReadLine();
            if (line == null) return false;
            linePieces = line.Split(' ');

            for (int i = 0; i < 5; i++) {
                hand1[i] = new Card();
                hand1[i].Value = getCardValue(linePieces[i].Substring(0, 1));
                hand1[i].Suit = getSuit(linePieces[i].Substring(1, 1));
            }

            for (int i = 0; i < 5; i++) {
                hand2[i] = new Card();
                hand2[i].Value = getCardValue(linePieces[i + 5].Substring(0, 1));
                hand2[i].Suit = getSuit(linePieces[i + 5].Substring(1, 1));
            }

            return true;
        }

        private static Suit getSuit(string suit) {
            if (suit == "D") return Suit.Diamond;
            if (suit == "C") return Suit.Club;
            if (suit == "H") return Suit.Heart;
            return Suit.Spade;
        }

        private static int getCardValue(string value) {

            int intvalue;
            if (Int32.TryParse(value, out intvalue)) return intvalue;

            if (value == "T") return 10;
            if (value == "J") return 11;
            if (value == "Q") return 12;
            if (value == "K") return 13;
            if (value == "A") return 14;

            return 0;
        }

        private class Card : IComparable {
            public Suit Suit { get; set; }
            public int Value { get; set; }

            public int CompareTo(object o) {
                if (o is Card) {
                    Card c = (Card)o;
                    if (Value < c.Value)
                        return -1;
                    else if (Value > c.Value)
                        return 1;
                    return 0;
                }
                throw new ArgumentException("Object is not a Card");
            }
        }
    }
}
