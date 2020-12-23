(ns day_22.solution
  (:require [clojure.string :as str]
            [main :as main :refer [defoverload]]))

(def day "22")

(defn get-lines
  "Read in and parse inputs as seq of vectors of ints."
  [file]
  (->> file
       slurp
       (#(str/split % #"(Player 1:\n)|(Player 2:\n)"))
       (map #(when-not (= "" %)
               (str/split % #"\n")))
       (remove nil?)
       (map #(for [x %] (read-string x)))))

(defn play-combat
  "Actually play a combat space card game given 2 decks."
  [[deck-1 deck-2]]
  (letfn [(compute-score [coll]
            (let [n (count coll)]
              (map * coll (range n 0 -1))))]
    (loop [deck-1 deck-1
           deck-2 deck-2]
      (if (and (seq deck-1)
               (seq deck-2))
        (let [[a b] (map first [deck-1 deck-2])]
          (if (> a b)
            ;; notice that conjoining to a vector is done at the end
            ;; but conjoining to a list is done at the beginning!!
            ;; a wins
            (recur (conj (vec (rest deck-1)) a b) (rest deck-2))
            ;; b wins
            (recur (rest deck-1) (conj (vec (rest deck-2)) b a))))
        (->> [deck-1 deck-2]
             (remove empty?)
             first
             ;; compute the scores from the result deck
             compute-score
             ;; sum up the scores
             (reduce +))))))

(defn play-recursive-combat
  "Actually play a combat space card game given 2 decks."
  [[deck-1 deck-2]]
  (letfn [(compute-score [coll]
            (let [n (count coll)]
              (map * coll (range n 0 -1))))]
    (loop [deck-1 deck-1
           deck-2 deck-2]
      (if (and (seq deck-1)
               (seq deck-2))
        (let [[a b] (map first [deck-1 deck-2])]
          (if (> a b)
            ;; notice that conjoining to a vector is done at the end
            ;; but conjoining to a list is done at the beginning!!
            ;; a wins
            (recur (conj (vec (rest deck-1)) a b) (rest deck-2))
            ;; b wins
            (recur (rest deck-1) (conj (vec (rest deck-2)) b a))))
        (->> [deck-1 deck-2]
             (remove empty?)
             first
             ;; compute the scores from the result deck
             compute-score
             ;; sum up the scores
             (reduce +))))))

(defn part1
  [_]
  (let [inputs (get-lines "day_22/inputs.txt")]
    (play-combat inputs)))

(defn part2
  [_]
  nil)

(defoverload main/part1 day part1)
(defoverload main/part2 day part2)
